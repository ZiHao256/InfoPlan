source /usr/local/gpdb/greenplum_path.sh

cd /home/zihao/arena/ARENA_system/back_end/gpdb_src

echo "compile GreenPlum ..."
sudo make
if [ $? = '0' ] 
then
    echo "compile success"
else
    echo "compile fail"
    exit 1
fi

echo "install GreenPlum ..."
sudo make install
if [ $? = '0' ] 
then
    echo "install success"
else
    echo "install fail"
    exit 1
fi

gpstop -d /home/zihao/gpDatabase/gpmaster/gpsne-1/ << :
Y
:
gpstart -d /home/zihao/gpDatabase/gpmaster/gpsne-1/ << :
Y
N
:

