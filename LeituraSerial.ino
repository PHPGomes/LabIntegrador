void setup() {
  Serial.begin(115200);
}

void loop() {
  float angulo = obterAnguloEncoder(); // sua função para ler o encoder
  Serial.println(angulo); // envia para o PC
  delay(50); // taxa de atualização
}
