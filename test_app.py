from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    bmi = None
    category = None
    color = None
    bg_color = None

    if request.method == 'POST':
        try:
            height = float(request.form['height'])
            weight = float(request.form['weight'])
            bmi = round(weight / ((height / 100) ** 2), 2)

            if bmi < 18.5:
                category = 'Underweight'
                color = 'blue'
                bg_color = '#d0e7ff'
            elif 18.5 <= bmi < 24.9:
                category = 'Normal'
                color = 'green'
                bg_color = '#d4f4dd'
            elif 25 <= bmi < 29.9:
                category = 'Overweight'
                color = 'orange'
                bg_color = '#ffe7c0'
            else:
                category = 'Obese'
                color = 'red'
                bg_color = '#ffcccc'
        except ValueError:
            bmi = None
            category = "Invalid input"
            color = "black"
            bg_color = "#f0f0f0"

    return render_template('index.html', bmi=bmi, category=category, color=color, bg_color=bg_color)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
