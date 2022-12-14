
a1 = [95,85,95,85,75,85,95,95,85,85,85,85];
a1=a1';
b1 = [2,2,1,2.5,1,1,2,2,2,2.5,3,16];
b1=b1';

for i=1:length(a1)
    if a1(i)>=97
       g1(i)=b1(i)*4;
    elseif a1(i)>=93
        g1(i)=b1(i)*3.94;
    elseif a1(i)>=90
        g1(i)=b1(i)*3.85;
    elseif a1(i)>=87
        g1(i)=b1(i)*3.73;
    elseif a1(i)>=83
        g1(i)=b1(i)*3.55;
    elseif a1(i)>=80
        g1(i)=b1(i)*3.32;
    elseif a1(i)>=77
        g1(i)=b1(i)*3.09;
    elseif a1(i)>=73
        g1(i)=b1(i)*2.78;
    elseif a1(i)>=70
        g1(i)=b1(i)*2.42;
    elseif a1(i)>=67
        g1(i)=b1(i)*2.08;
    elseif a1(i)>=63
        g1(i)=b1(i)*1.63;
    elseif a1(i)>=60
        g1(i)=b1(i)*1.15;
    else
        g1(i)=0;
    end
end

a = [95,84,77,84,79,84,84,87,86,69,78,76,90,82,85,72,64,68,64,84,72,86,72,95,71,86,80,80,63,73,75,63,76,82,90,83,78,71,82,81,74,82,84,78,85,78,77,80];
a = a';
b = [0.75,2,4,5,4,0.75,2,2,4,3,5,3,0.75,4,1,3,7,3.5,3,5,3,0.75,1,0.75,3,3,3.5,3,3,3,2.5,2,3.5,3,2,2.5,2.75,2.5,3.75,2.5,2.75,2,5,2,1,2.5,3.5,2];
b = b';

for i = 1 : length(b)
    if a(i) == 95
        g(i) = b(i) * 3.95;
    end
    if a(i) == 94
        g(i) = b(i) * 3.93;
    end
    if a(i) == 93
        g(i) = b(i) * 3.91;
    end
    if a(i) == 92
        g(i) = b(i) * 3.88;
    end
    if a(i) == 91
        g(i) = b(i) * 3.85;
    end
    if a(i) == 90
        g(i) = b(i) * 3.81;
    end
    if a(i) == 89
        g(i) = b(i) * 3.77;
    end
    if a(i) == 88
        g(i) = b(i) * 3.73;
    end
    if a(i) == 87
        g(i) = b(i) * 3.68;
    end
    if a(i) == 86
        g(i) = b(i) * 3.63;
    end
    if a(i) == 85
        g(i) = b(i) * 3.58;
    end
    if a(i) == 84
        g(i) = b(i) * 3.52;
    end
    if a(i) == 83
        g(i) = b(i) * 3.46;
    end
    if a(i) == 82
        g(i) = b(i) * 3.39;
    end
    if a(i) == 81
        g(i) = b(i) * 3.32;
    end
    if a(i) == 80
        g(i) = b(i) * 3.25;
    end
    if a(i) == 79
        g(i) = b(i) * 3.17;
    end
    if a(i) == 78
        g(i) = b(i) * 3.09;
    end
    if a(i) == 77
        g(i) = b(i) * 3.01;
    end
    if a(i) == 76
        g(i) = b(i) * 2.92;
    end
    if a(i) == 75
        g(i) = b(i) * 2.83;
    end
    if a(i) == 74
        g(i) = b(i) * 2.73;end
    if a(i) == 73
        g(i) = b(i) * 2.63;end
    if a(i) == 72
        g(i) = b(i) * 2.53;end
    if a(i) == 71
        g(i) = b(i) * 2.42;end
    if a(i) == 70
        g(i) = b(i) * 2.31;end
    if a(i) == 69
        g(i) = b(i) * 2.20;end
    if a(i) == 68
        g(i) = b(i) * 2.08;end
    if a(i) == 67
        g(i) = b(i) * 1.96;end
    if a(i) == 66
        g(i) = b(i) * 1.83;end
    if a(i) == 65
        g(i) = b(i) * 1.70;end
    if a(i) == 64
        g(i) = b(i) * 1.57;end
    if a(i) == 63
        g(i) = b(i) * 1.43;end
    if a(i) == 62
        g(i) = b(i) * 1.29;end
    if a(i) == 61
        g(i) = b(i) * 1.15;end
    if a(i) == 60
        g(i) = b(i) * 1.00;end
end
g
g1
sum(b1);
sum(b);

ave_score = (sum(a1)+sum(a))/(length(a1)+length(a))
GPA=(sum(g1)+sum(g))/(sum(b1)+sum(b))