from flask import flash, redirect, url_for, render_template

from sayhello import app, db
from sayhello.forms import HelloForm
from sayhello.models import Message


@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))

    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', form=form, messages=messages)


@app.route('/message/<int:message_id>', methods=['GET'])
def message(message_id):
    message = Message.query.get_or_404(message_id)
    return render_template('message.html', message=message)

@app.route('/api/v1/messages', methods=['GET'])
def api_messages():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return {'messages': [{'name': message.name, 'body': message.body} for message in messages]}