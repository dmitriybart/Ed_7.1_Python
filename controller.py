import view as v
import data_base as db
import funcs as f

def click():
    numb1 = v.number()
    numb2 = v.number()
    op = v.operator()
    db.write_data(numb1, numb2, op)
    res = f.do_it(db.read_data())
    db.write_data_res(res)
    v.view_data(res)