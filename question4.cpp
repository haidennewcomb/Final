// Grade Calculator
// A.I Disclaimer: Some, I used A.I to fix syntax errors
#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    double homeworkAverage;
    double finalExamGrade;
    double finalPercentage;
    char letterGrade;

    // Get user input
    cout << "Enter homework average: ";
    cin >> homeworkAverage;

    cout << "Enter final exam grade: ";
    cin >> finalExamGrade;

    finalPercentage = (homeworkAverage * 0.80) + (finalExamGrade * 0.20);

    if (finalPercentage >= 90) {
        letterGrade = 'A';
    }
    else if (finalPercentage >= 80) {
        letterGrade = 'B';
    }
    else if (finalPercentage >= 70) {
        letterGrade = 'C';
    }
    else if (finalPercentage >= 60) {
        letterGrade = 'D';
    }
    else {
        letterGrade = 'F';
    }

    cout << fixed << setprecision(1);
    cout << "\nFinal percentage: " << finalPercentage << endl;
    cout << "Letter grade: " << letterGrade << endl;

    if (letterGrade == 'A') {
        cout << "Excellent job! You earned an A." << endl;
    }
    else if (letterGrade == 'B') {
        cout << "Nice work. You finished strong." << endl;
    }
    else if (letterGrade == 'C') {
        cout << "Good effort. Keep improving." << endl;
    }
    else if (letterGrade == 'D') {
        cout << "You passed, but there’s room to improve." << endl;
    }
    else {
        cout << "You may need extra help next time." << endl;
    }

    return 0;
}