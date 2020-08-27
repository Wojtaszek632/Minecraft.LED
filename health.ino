#include <Adafruit_NeoPixel.h>

#define Led_Pin 6
#define Led_Count 10
Adafruit_NeoPixel strip(Led_Count, Led_Pin, NEO_GRB + NEO_KHZ800);

int hp_buff[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

void refresh_hp(int arg_health_todisplay)
{
    if (arg_health_todisplay <= 20 && arg_health_todisplay >= 0)
    {
        memset(hp_buff, 0, sizeof(hp_buff));
        for (int i = 0; i < arg_health_todisplay; i++)
        {
            hp_buff[(i / 2)] = (hp_buff[(i / 2)] * 8) + 25;
        }
    }
}
void setup()
{
    Serial.begin(9600);
    strip.begin();
    strip.show();
}
char CHAR_incomingByte;
int INT_incomingByte = 0;
String str;
void loop()
{
    if (Serial.available() > 0)
    {
        //CHAR_incomingByte = Serial.read();
        str = Serial.readStringUntil('\n');
        //INT_incomingByte = Serial.
        Serial.println(str);
        refresh_hp(str.toInt());
    }

    for (int y = 0; y < 10; y++)
    {
        strip.setPixelColor(y, hp_buff[y], 0, 0);
    }
    strip.show();
    delay(50);
}
