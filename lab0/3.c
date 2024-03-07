#include <stdio.h>

struct Stan {
    int x, y;
    void (*foo)(struct Stan *);
};

void state1(struct Stan *ptr) {
    printf("Stan: %i\n", ptr->y);
}

void state2(struct Stan *ptr) {
    printf("Stan: %i\n", ptr->y);
}

int main() {
    struct Stan P[] = {{1, 1, &state1}, {1, 2, &state2}};
    int N = sizeof(P) / sizeof(struct Stan);

    for (int i = 0; i < N; i++) {
        if (P[i].x == 1) {
            (P[i].foo)(&P[i]); // Poprawiona linia
        }
    }

    return 0;
}
