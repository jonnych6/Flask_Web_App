from website import create_app

app = create_app()

if __name__ == '__main__': #only if this file is ran vs imported will this line run
    app.run(debug=True) #debug = everytime we make a change to python code, it will auto rerun the server. Turn off during production