from flask import Flask, flash, render_template, request

from card_look_up import card_look_up

app=Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def return_chi_mtg_cards():

    chi_cards = None

    def blank_card_page():
        return render_template('index.html',
                               card_name=None,
                               chi_cards=None)

    if request.method == 'GET':
        return blank_card_page()

    if request.method == 'POST':
        #return blank_card_page()
        try:
            search_card = request.form['cardsearch']
            if search_card == 'none':
                flash('Please enter a card')
            else:
                try:
                    chi_cards = card_look_up(search_card)
                except Exception as e:
                    flash(e)
        except Exception:
            print e
            return blank_card_page()

        if chi_cards:
                return render_template('index.html',
                                       card_name=search_card,
                                       chi_cards=chi_cards)

if __name__ == '__main__':
    app.run(host='0.0.0.0')