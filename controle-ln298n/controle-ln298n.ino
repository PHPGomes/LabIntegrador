// Definições de pinos (Conferir no esquemático)
#define IN1  30   // Controle do motor - direção
#define IN2  31   // Controle do motor - direção
#define PWM  29   // PWM (velocidade)

bool dieita;

void setup() {
  pinMode(IN1,OUTPUT);
  pinMode(IN2,OUTPUT);
  pinMode(PWM,OUTPUT);
  dieita = false;
}

void loop() {
  
}


void Controle(float sinal){
  if(sinal>=0){
    movDireita(map(sinal,0,1,0,255));//map(valor, deMenor, deMaior, paraMenor, paraMaior); confirmar sinal de controle para arrumar
  }
  else{
    movEsquerda(map(-sinal,0,1,0,255));//map(valor, deMenor, deMaior, paraMenor, paraMaior); confirmar sinal de controle para arrumar
  }
}


void movDireita(int pwm){
  if(dieita){
    digitalWrite(IN1,LOW);
    digitalWrite(IN2,HIGH);
    analogWrite(PWM,pwm);
  }
  else{  
    digitalWrite(PWM,LOW);
    delay(20);
    digitalWrite(IN1,LOW);
    delay(20);
    digitalWrite(IN2,HIGH);
    analogWrite(PWM,pwm);
    }
  direita = true;
}


void movEsquerda(int pwm){
  if(direita){
    digitalWrite(PWM,LOW);
    delay(20);
    digitalWrite(IN2,LOW);
    delay(20);
    digitalWrite(IN1,HIGH);
    analogWrite(PWM,pwm);
  }
  else{
    digitalWrite(IN2,LOW);
    digitalWrite(IN1,HIGH);
    analogWrite(PWM,pwm);
  }
  direita = false;
}
