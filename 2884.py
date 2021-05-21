# H,M = map(int,input().split())
# if H >= 0 and M >= 45:
#     print(f'{H-1} {M-45}')

# elif H >= 0 and M>=30:
#     print(f'{H+23} {M+15}')

# else:
#     print(f'{H-1} {M+15}')




H,M = map(int, input().split())


if M > 44:    
    print(H, M-45)  
elif M <= 44 and H >= 1:
    print(H-1, M+15)
else:
    print(23, M+15)
