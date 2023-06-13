from eve import Eve
app = Eve(settings='settings.py')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
