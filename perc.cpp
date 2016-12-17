#include <iostream>
#include <vector>
#include <time.h>
#include <stdlib.h>

class Perceptron
{

public:
	std::vector<float> weights;
	float c=0.001;
	int activate(int sum){
		return sum>0?1:-1;
	}
	void Make(int n){

		weights.resize(n);

		for (int i=0; i<weights.size(); i++){
			weights[i]=2*((float) rand()-RAND_MAX/2)/RAND_MAX;
			// std::cout<<weights[i]<<"\n";
		}
	}

		int feedforward(std::vector<float> inputs){
			//assert inputs.size()=weights.size();
			float sum=0;
			for(int i=0; i<inputs.size(); i++){
				sum+=inputs[i]*weights[i];
			}
			return activate(sum);
		}

		void train(std::vector<float> inputs, int desired){
			int guess=feedforward(inputs);
			float error=desired-guess;
			for (int i=0; i<weights.size(); i++){
				// std::cout<<weights[i]<<" ";
				weights[i]+=c*error*inputs[i];
			}
		}

};

class Trainer{


	float f(float x){
		return m*x+b;

	}
	void MakeTrain(float x, float y, int a){
		inputs.resize(3);
		inputs[0]=x;
		inputs[1]=y;
		inputs[2]=1;
		answer=a;
		// std::cout<<inputs[0]<<" "<<inputs[1]<<" "<<inputs[2]<<" "<<answer<<"\n";
	}
public:
	float m=2;
	float b=1;
	std::vector<float> inputs;
	int answer;

	void PercTrainer(void){
		int width=25/m; //x value
		int height=25;
		float x=rand()%width-width/2;
		float y=rand()%height-height/2;
		float yline=f(x);
		int a;
		if(y<yline){
			a=-1; //desired answer
		} else{
			a=1; //desired answer
		}
		MakeTrain(x,y,a);

	}




};



int main(){
	srand((unsigned) time(NULL));
	Perceptron perc;
	perc.Make(3);
	Trainer t[2000];
	for(int i=0; i<2000; i++){
		t[i].PercTrainer();
		perc.train(t[i].inputs, t[i].answer);
	}
	printf("%.5f %d \n", -t[0].m, 1);

	std::cout<<perc.weights[0]/perc.weights[1]<<" "<<1<<"\n";


	return 0;
}
