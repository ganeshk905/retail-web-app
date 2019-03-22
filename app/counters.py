emp_counter = 0
dept_counter = 0
role_counter = 0
cust_counter = 0
stcok_counter = 0
prod_counter = 0
pc_counter = 0
sales_counter = 0
sc_counter = 0
df_counter = 0
quant_counter = 0
expenses_counter = 0
ec_counter = 0
st_counter = 0

def get_next_employee_id():
    global emp_counter
    emp_counter = emp_counter+1
    return emp_counter

def get_next_department_id():
    global dept_counter
    dept_counter = dept_counter+1
    return dept_counter

def get_next_role_id():
    global role_counter
    role_counter = role_counter+1
    return role_counter

def get_next_stock_id():
    global stcok_counter
    stcok_counter = stcok_counter+1
    return stcok_counter

def get_next_product_id():
    global prod_counter
    prod_counter = prod_counter+1
    return prod_counter

def get_next_pc_id():
    global pc_counter
    pc_counter = pc_counter+1
    return pc_counter

def get_next_cust_id():
    global cust_counter
    cust_counter = cust_counter+1
    return cust_counter

def get_next_sales_id():
    global sales_counter
    sales_counter = sales_counter+1
    return sales_counter

def get_next_sc_id():
    global sc_counter
    sc_counter = sc_counter+1
    return sc_counter

def get_next_df_id():
    global df_counter
    df_counter = df_counter+1
    return df_counter

def get_next_quant_id():
    global quant_counter
    quant_counter = quant_counter+1
    return quant_counter

def get_next_expenses_id():
    global expenses_counter
    expenses_counter = expenses_counter+1
    return expenses_counter

def get_next_ec_id():
    global ec_counter
    ec_counter = ec_counter+1
    return ec_counter

def get_next_st_id():
    global st_counter
    st_counter = st_counter+1
    return st_counter