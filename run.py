from app import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        print("Hello Flask")
        db.create_all()
    app.run(debug=True,use_reloader=False)