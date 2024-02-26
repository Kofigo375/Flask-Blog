from flaskblog import app

## if we want to run this script with python directly
if __name__ == '__main__':
    app.run(debug=True)

## two ways of runing flask apps 
## 1. set environment variables
## 2. including app.run in main app script
