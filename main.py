import Lib
import VariableCommune
from app.back.Home import run_app
from BDD.Creation.CreateTable import CreateTable
from BDD.Creation.CreateDB import CreateDB
#import pages.UserConnection as UserConnection

def main():
    Lib.st.set_page_config(
        page_title="Home",
        page_icon=":house:",
    )

    Lib.st.write("# Welcome to the Home page! 👋")
    CreateDB()
    CreateTable()

    Lib.st.write("## Please select an option from the sidebar to get started.")
    Lib.st.write("You can also create your user account by clicking on the 'Create Account' option.")
    return

if __name__ == "__main__":
    main()