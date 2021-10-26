#include<stdio.h>
void UnsortedMissing(int a[],int nsize,int b[],int h,int l){
	int i,j,ele,k;
	for(i=0;i<=h;i++){
		b[i]=0;
	}
	for(j=0;j<nsize;j++){
		ele=a[j];
		b[ele]=1;
	}
	for(k=l;k<h;k++){
		if(b[k]!=1){
			printf("The Missing element is %d\n",k);
		}
	}
}
int main(){
	int i,n,max,min;
	int a[100], b[100];
	printf("Enter the size of the array\n");
	scanf("%d",&n);
	printf("Enter the elements in the array\n");
	for(i=0;i<n;i++){
		scanf("%d",&a[i]);
	}
	max=a[0];
	for(i=1;i<n;i++){
		if(a[i]>max){
			max=a[i];
		}
	}
	min=a[0];
	for(i=0;i<n;i++){
		if(a[i]<min){
			min=a[i];
		}
	}
	UnsortedMissing(a,n,b,max,min);
}
