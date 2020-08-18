# SOEN287 Web Programming Take-Home Final Exam
# Winter 2020
import csv
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField, PasswordField, BooleanField, RadioField
from wtforms.validators import InputRequired, Email, DataRequired, Length, EqualTo
app = Flask(__name__)

app.secret_key = 'allo'



# TODO: Question 2: Survey FlaskForm
# Write your survey FlaskForm starting on the next line
class SurveyForm(FlaskForm):
    Email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    EmailHidden = BooleanField('EmailHidden')
    FavouriteColor= StringField("FavouriteColor", validators=[InputRequired("Please")])
    ChooseAFood= RadioField("ChooseAFood", validators=[InputRequired()], choices=[('a', 'Pizza'),('b', 'Ramen'),('c', 'Pasta'),('d', 'Dimsum')])
# end of your survey FlaskForm


@app.route('/')
def exam():
    return render_template('exam.html', has_prev=False, has_next=False )


# TODO: Question 1: questions endpoints
# Routes for the 4 questions templates starting on the next line
@app.route('/q1.html')
def q1():
    next= '/q2.html'
    return render_template('q1.html', has_prev=False, has_next=True, next=next)

@app.route('/q2.html')
def q2():
    back= '/q1.html'
    next='/q3.html'
    return render_template('q2.html', has_prev=True, has_next=True, back=back, next=next)

@app.route('/q3.html')
def q3():
    back= '/q2.html'
    next='/q4.html'
    return render_template('q3.html', has_prev=True, has_next=True, back=back, next=next)

@app.route('/q4.html')
def q4():
    back= '/q3.html'
    return render_template('q4.html', has_prev=True, has_next=False, back=back)
# End of the 4 questions templates


# TODO: Question 2: Survey Endpoint
# Write your survey endpoint starting on the next line
@app.route('/survey', methods=['GET', 'POST'])
def survey():
    form = SurveyForm()
    if form.validate_on_submit():
        if form.EmailHidden.data is True:
            with open('messages.csv', 'a',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['hidden', form.FavouriteColor.data, form.ChooseAFood.data])
            return redirect('/results')
        else:
            with open('messages.csv', 'a',newline='') as f:
                writer = csv.writer(f)
                writer.writerow([form.Email.data,form.FavouriteColor.data, form.ChooseAFood.data])
            return redirect('/results')
    return render_template('survey.html', form=form,has_prev=False, has_next=False)
# end of your survey endpoint


# TODO: Question 3: Survey Results Endpoint
# Write your survey results endpoint starting on the next line
@app.route('/results')
def results():
    with open('messages.csv', 'r') as f:
        reader= csv.reader(f)
        results=[]
        number=0
        SplittedResult=[]
        email= []
        numberOfAnonymous=0
        numberOfA=0
        numberOfB=0
        numberOfC=0
        numberOfD=0
        for line in reader:
            results.append(line)
            number +=1
            if line[0]=='hidden':
                numberOfAnonymous +=1
            if line[2]=='a':
                numberOfA+=1
            elif line[2]=='b':
                numberOfB+=1
            elif line[2]=='c':
                numberOfC+=1
            else:
                numberOfD+=1

        percentage_of_a= round(numberOfA/number, 3)*100
        percentage_of_b= round(numberOfB/number, 3)*100
        percentage_of_c= round(numberOfC/number, 3)*100
        percentage_of_d= round(numberOfD/number, 3)*100
        percentage_of_Anonymous= round(numberOfAnonymous/number, 2)*100
        return render_template('results.html',has_prev=False, has_next=False, results=results, number= number,numberOfAnonymous=numberOfAnonymous, numberOfA= numberOfA, numberOfB= numberOfB, numberOfC= numberOfC, numberOfD= numberOfD, percentage_of_a= percentage_of_a,
        percentage_of_b= percentage_of_b, percentage_of_c= percentage_of_c, percentage_of_d= percentage_of_d, percentage_of_Anonymous= percentage_of_Anonymous)
# end of your survey results endpoint


# TODO: Question 4: JavaScript and regular expressions
# Write your postal codes endpoint starting on the next line
@app.route('/codes')
#in development :p
def codes():
    return render_template('codes.html')
# end of your postal codes endpoint


if __name__ == '__main__':
    app.run(debug=True)
