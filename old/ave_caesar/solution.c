#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define STRING_SIZE 1000000

char* getString() {
	char* string = malloc(STRING_SIZE * sizeof(*string));

	scanf("%s", string);

	int length = strlen(string);
	string = realloc(string, length+1 * sizeof(*string));

	return string;
}

int compareStrings(char* s1, char* s2, int s1Len, int s2Len) {
	int length = s1Len>=s2Len ? s1Len : s2Len;
	for (int i=0; i<length; i++) {
		char c1 = i<=s1Len ? s1[i] : ' ';
		char c2 = i<=s2Len ? s2[i] : ' ';
		int difference = c1 - c2;
		if (difference != 0) return difference;
	}

	return 0;
}

int isValidString(char* string, int stringLength) {
	if (stringLength == 1){
		return 1;
	}

	for (int i=1; i<stringLength; i++) {
		char* s1 = string;
		int s1Length = i;

		char* s2 = string + i;
		int s2Length = stringLength-s1Length;

		if (compareStrings(s1, s2, s1Length, s2Length) > 0) continue;

		if (!isValidString(s1, s1Length) || !isValidString(s2, s2Length)) continue;

		if (compareStrings(s1, s2, s1Length, s2Length) <= 0) return 1;
	}

	return 0;
}

int main() {
	int N;
	scanf("%d", &N);

	char* output = calloc(N, sizeof(*output));

	for (int i=0; i<N; i++) {
		char* string = getString();

		if (isValidString(string, strlen(string))) {
			output[i] = '1';
		} else {
			output[i] = '0';
		}

		free(string);
	}

	puts(output);
}
