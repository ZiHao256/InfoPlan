source /usr/local/gpdb/greenplum_path.sh


gpstop -d /home/zihao/gpDatabase/gpmaster/gpsne-1/ << :
Y
:
gpstart -d /home/zihao/gpDatabase/gpmaster/gpsne-1/ << :
Y
N
:

