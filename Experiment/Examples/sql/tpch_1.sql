select
    s_acctbal, s_name, n_name, s_address, s_phone, s_comment
from
    supplier, nation, region
where
    s_acctbal>=5000
    and n_name = 'CHINA'
    and s_nationkey = n_nationkey
    and n_regionkey = r_regionkey
;