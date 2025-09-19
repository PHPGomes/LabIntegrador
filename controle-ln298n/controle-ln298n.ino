// Definições de pinos (Conferir no esquemático)
#define IN1  26   // Controle do motor - direção
#define IN2  27   // Controle do motor - direção
#define PWM  14   // PWM (velocidade)

bool dieita;

void setup() {
  pinMode(IN1,OUTPUT);
  pinMode(IN2,OUTPUT);
  pinMode(PWM,OUTPUT);
  dieita = false;
}

void loop() {
  
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
