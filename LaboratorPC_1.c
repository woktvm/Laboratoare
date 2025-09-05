#include <stdio.h>
#include <math.h>
int main()
{
	float a,b,c,x;
	float F;
	printf("Introdu variabilele pentru operatie a,b,c si x: \n");
	scanf("%d %d %d %d", &a, &b, &c, &x);
	if(x<0 && b !=0){
	    F =  a-cos(x)/(10+b);
        printf("Rezultatul este: %f\n", F);
	} else if(x>0 || b == 0){
	    F = (x-a)/(x-b);
	    printf("Rezultatul este: %f\n", F);
	} else {
	    F = 3*pow(x,2) + a/c;
	    printf("Rezultatul este: %f\n", F);
	}
 

	return 0;
}