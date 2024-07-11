
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cstdio>

using namespace std;

bool validateLogin(const string &username, const string &password)
{
    // Replace this with a database or some secure method of validating the credentials
    return (username == "user" && password == "password");
}

void login()
{
    int attempts = 0;
    const int maxAttempts = 3;

    do
    {
        system("cls"); // Use a more portable method for clearing the screen

        cout << "\n\n   **************************";
        cout << "\n\t   Welcome my Intelligent People";
        cout << "\n   **************************\n";
        cout << "\n   ----------------------------";
        cout << "\n   LOGIN FORM";
        cout << "\n   ----------------------------";
        cout << "\n\n   ENTER USERNAME: ";
        string username;
        cin >> username;

        cout << " \n   ENTER PASSWORD: ";
        string password;
        char c;
        while (true)
        {
            c = _getch();
            if (c == 13) // Enter key
                break;
            password += c;
            cout << "*"; // Mask the password input
        }

        if (validateLogin(username, password))
        {
            cout << "\n\n   **************************";
            cout << "\n   WELCOME USER !!!!";
            cout << "\n   **************************\n";
            cout << "\n   Press any key to continue...";
            _getch();
            break;
        }
        else
        {
            cout << "\n\n   ----------------------------";
            cout << "\n   LOGIN IS UNSUCCESSFUL...PLEASE TRY AGAIN...";
            attempts++;
            _getch();
        }
    } while (attempts < maxAttempts);

    if (attempts >= maxAttempts)
    {
        cout << "\nSorry, you have entered the wrong username and password " << maxAttempts << " times!!!";
        _getch();
        exit(1); // Exit the program after too many login attempts
    }
}

void askQuestions()
{
    cout << "Answer the following questions to jazz yourself:\n";

    string answer;

    // You can add more questions as needed
    cout << "1. What's your favorite color? ";
    cin >> answer;
    cout << "Your favorite color is: " << answer << endl;

    cout << "2. What's your favorite hobby? ";
    cin >> answer;
    cout << "Your favorite hobby is: " << answer << endl;

    cout << "3. What's your favorite food? ";
    cin >> answer;
    cout << "Your favorite food is: " << answer << endl;
}

void happyMode()
{
    // Implement the Happy mode actions here
    cout << "You selected Happy mode.\n";

    // Add your Happy mode logic here
    cout << "Happy mode logic: Everything is fun and exciting!\n";

    // Ask questions to jazz the user
    askQuestions();
}

void boringMode()
{
    // Implement the Boring mode actions here
    cout << "You selected Boring mode.\n";

    // Add your Boring mode logic here
    cout << "Boring mode logic: Everything is calm and ordinary.\n";

    // Ask questions to jazz the user
    askQuestions();
}

void outdoorAdventureMode()
{
    // Implement the Outdoor Adventure mode actions here
    cout << "You selected Outdoor Adventure mode.\n";

    // Add your Outdoor Adventure mode logic here
    cout << "Outdoor Adventure mode logic: Describe your ideal outdoor adventure!\n";

    // Ask the user to describe their ideal outdoor adventure
    cout << "Describe your ideal outdoor adventure: ";
    string adventure;
    cin.ignore(); // Clear newline from previous input
    getline(cin, adventure);
    cout << "Your ideal outdoor adventure:\n"
         << adventure << endl;

    // You can add more questions or tasks related to outdoor adventures as needed
}

void mode()
{
    char choice;
    do
    {
        system("cls");
        cout << "Select your mode:\n";
        cout << "\ta. Happy\n";
        cout << "\tb. Boring\n";
        cout << "\tc. Creative\n";          // Add Creative mode option
        cout << "\td. Outdoor Adventure\n"; // Add Outdoor Adventure mode option
        cout << "\te. Exit\n";              // Changed 'd' to 'e' for Exit option
        cout << "Your choice: ";
        cin >> choice;

        switch (choice)
        {
        case 'a':
            happyMode(); // Call the Happy mode function
            break;
        case 'b':
            boringMode(); // Call the Boring mode function
            break;
        case 'c':
            creativeMode(); // Call the Creative mode function
            break;
        case 'd':
            outdoorAdventureMode(); // Call the Outdoor Adventure mode function
            break;
        case 'e':
            cout << "Exiting the program.\n";
            exit(0);
        default:
            cout << "Invalid choice. Please select a valid mode (a, b, c, d, or e).\n";
            _getch();
        }
    } while (true);
}

void creativeMode()
{
    // Implement the Creative mode actions here
    cout << "You selected Creative mode.\n";

    // Add your Creative mode logic here
    cout << "Creative mode logic: Let your imagination run wild!\n";

    // Ask creative questions or provide creative tasks
    cout << "Create a short story: ";
    string story;
    cin.ignore(); // Clear newline from previous input
    getline(cin, story);
    cout << "Your creative story:\n"
         << story << endl;

    // You can add more creative tasks or questions as needed
}

int main()
{
    login();
    mode();

    return 0;
}
