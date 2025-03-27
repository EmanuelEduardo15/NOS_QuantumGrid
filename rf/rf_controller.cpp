#include <LimeSuite.h>
#include <iostream>

void configure_5g(double freq, double bw) {
    lms_device_t* dev;
    LMS_Open(&dev, NULL, NULL);
    LMS_Init(dev);
    LMS_SetSampleRate(dev, bw * 1e6, 0);
    LMS_SetLOFrequency(dev, LMS_CH_TX, 0, freq * 1e6);
    LMS_EnableChannel(dev, LMS_CH_TX, 0, true);
}

int main() {
    configure_5g(3500.0, 100.0);
    return 0;
}
