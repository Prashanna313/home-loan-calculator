from flask import Flask, render_template, request, send_file, session, redirect, url_for
import pandas as pd
import io

app = Flask(__name__)
app.secret_key = 'supersecret'  # Required to use session

def calculate_emi(principal, annual_rate, tenure_months):
    monthly_rate = annual_rate / 12 / 100
    emi = principal * monthly_rate * (1 + monthly_rate) ** tenure_months / ((1 + monthly_rate) ** tenure_months - 1)
    return emi

def schedule_from_emi(principal, annual_rate, emi):
    monthly_rate = annual_rate / 12 / 100
    balance = principal
    schedule = []
    total_interest = 0
    month = 0

    while balance > 0:
        interest = balance * monthly_rate
        principal_paid = emi - interest
        if principal_paid > balance:
            principal_paid = balance
            emi = interest + principal_paid
        balance -= principal_paid
        total_interest += interest
        month += 1
        schedule.append({
            "Month": month,
            "EMI": round(emi, 2),
            "Interest Paid": round(interest, 2),
            "Principal Paid": round(principal_paid, 2),
            "Remaining Balance": round(balance, 2)
        })

    return schedule, month, round(total_interest, 2)

def schedule_from_duration(principal, annual_rate, tenure_months):
    emi = calculate_emi(principal, annual_rate, tenure_months)
    monthly_rate = annual_rate / 12 / 100
    balance = principal
    schedule = []
    total_interest = 0

    for month in range(1, tenure_months + 1):
        interest = balance * monthly_rate
        principal_paid = emi - interest
        balance -= principal_paid
        total_interest += interest
        schedule.append({
            "Month": month,
            "EMI": round(emi, 2),
            "Interest Paid": round(interest, 2),
            "Principal Paid": round(principal_paid, 2),
            "Remaining Balance": round(balance, 2)
        })

    return schedule, round(emi, 2), round(total_interest, 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = {}
    if request.method == 'POST':
        mode = request.form['mode']
        principal = float(request.form['principal'])
        rate = float(request.form['rate'])

        if mode == 'emi':
            emi = float(request.form['emi'])
            schedule, months, total_interest = schedule_from_emi(principal, rate, emi)
            data = {
                "mode": "emi",
                "schedule": schedule,
                "months": months,
                "total_interest": total_interest
            }

        elif mode == 'duration':
            duration = int(request.form['duration'])
            schedule, emi, total_interest = schedule_from_duration(principal, rate, duration)
            data = {
                "mode": "duration",
                "schedule": schedule,
                "emi": emi,
                "total_interest": total_interest,
                "months": duration
            }

        # Save schedule for Excel export
        session['schedule'] = schedule
        session['mode'] = mode
        session['months'] = data.get("months")
        session['emi'] = data.get("emi")
        session['total_interest'] = data.get("total_interest")

    return render_template('index.html', data=data)
@app.route('/download')
def download_excel():
    schedule = session.get('schedule', [])
    if not schedule:
        return redirect(url_for('index'))

    df = pd.DataFrame(schedule)
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Repayment Schedule')

    output.seek(0)
    return send_file(output,
                     download_name='loan_schedule.xlsx',
                     as_attachment=True,
                     mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)