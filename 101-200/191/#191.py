n = 30
(v_0, v_1, v_2, v_L0, v_L1, v_L2) = (1, 1, 0, 1, 0, 0)
for _ in range(1, n):
    (v_0, v_1, v_2, v_L0, v_L1, v_L2) = (v_0 + v_1 + v_2,
        v_0,
        v_1,
        v_0 + v_1 + v_2 + v_L0 + v_L1 + v_L2,
        v_L0,
        v_L1)

print (sum([v_0, v_1, v_2, v_L0, v_L1, v_L2]))
#f[n] is the number of ways to get a prize 
#f[n]=2*f[n-1]+f[n-2]-3*f[n-4]-2*f[n-5]-f[n-6]