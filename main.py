import Lib
import VariableCommune
import pages.UserConnection as UserConnection
from app.back.Home import run_app
from BDD.Creation.CreateTable import CreateTable
from BDD.Creation.CreateDB import CreateDB

def main():
    CreateDB()
    CreateTable()
    Lib.st.set_page_config(
        page_title="Home",
        page_icon=":house:",
    )
    Lib.st.sidebar.header("Main Menu")

    Lib.st.write("# Welcome to the Home page! 👋")
    return

if __name__ == "__main__":
    main()