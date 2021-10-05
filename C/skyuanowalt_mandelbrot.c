// Calculates if number is within mandelbrot steps

int escapeSteps (double x, double y){
    int z = 0;
    int steps = 0;
    double a = 0.0;
    double b = 0.0;
    double real = 0.0;
    double unreal = 0.0;

    while (steps < maxSteps && z < setOut){
        // expansion of z
        // (a^2 - b^2 + x) + (2ab +y)i

        real = (a*a) - (b*b) + x;
        unreal = (2*a*b) + y;
        a = real;
        b = unreal; 
        z = (a*a) + (b*b);
        steps = steps + 1;
    }
    return steps;
}
