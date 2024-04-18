import Lib
import VariableCommune
from app.back.Temp import run_app
from BDD.Creation.CreateTable import CreateTable

def main():
    CreateTable()
    run_app()
    return

if __name__ == "__main__":
    main()