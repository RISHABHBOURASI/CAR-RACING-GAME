#include <iostream>
#include <conio.h>   // for _kbhit() and _getch()
#include <windows.h> // for Sleep()

using namespace std;

int carPos = 10;
int roadLeft = 5, roadRight = 20;
int score = 0;

void drawRoad() {
    system("cls");
    for (int i = 0; i < 20; i++) {
        for (int j = 0; j < 30; j++) {
            if (j == roadLeft || j == roadRight) cout << "|";
            else if (j == carPos && i == 18) cout << "A"; // Car at bottom
            else cout << " ";
        }
        cout << "\n";
    }
    cout << "Score: " << score << endl;
}

int main() {
    while (true) {
        if (_kbhit()) {
            char ch = _getch();
            if (ch == 'a' && carPos > roadLeft+1) carPos--;
            if (ch == 'd' && carPos < roadRight-1) carPos++;
            if (ch == 'q') break;
        }

        drawRoad();
        score++;
        Sleep(100);

        // Simulate road shifting
        int shift = rand() % 3 - 1; 
        roadLeft += shift;
        roadRight += shift;

        if (carPos <= roadLeft || carPos >= roadRight) {
            cout << "🚨 Crash! Game Over 🚨\n";
            break;
        }
    }
    return 0;
}
