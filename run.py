from password_manager import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='2.196.96.80', port=8080)