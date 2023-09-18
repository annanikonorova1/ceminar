from flask import Flask, render_template, request, flash, url_for, redirect

redirect, url_for
import os
from config import Config
from models import  User2
from random import choice
from flask_wtf.csrf import CSRFProtect
from forms import forma
@app.route('/forma/', methods=['GET', 'POST'])
def forma(db=User2):
    form = forma()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        name = form.name.data.lower()
        surname = form.surname.data.lower()
        email = form.email.data
        user = User2(name=name, surname=surname, email=email)
        if User2.query.filter(User2.email == email).first():
            flash(f'Пользователь с e-mail {email} уже существует')
            return redirect(url_for('registration'))
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Вы успешно зарегистрировались!')
        return redirect(url_for('forma'))
    return render_template('forma.html', form=form)


if __name__ == '__main__':
    app.run()