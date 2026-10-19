# 포함관계(in, not in)

role = 'admin'

# if role == 'admin' or role == 'manager' or role == 'staff'  -> role이 admin이나 manager거나 staff 라면

allowed_roles = ['admin', 'manager', 'staff']
if role in allowed_roles:   # in: allowed_roles 라는 집합에 포함 된다면
    print('접근 허용')
else:
    print('접근 불가')