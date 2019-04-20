for v in ../wxFormBuilder_MarkMedia/*.py
do
echo $v
f="$(basename -- $v)"
sed "s/\t /\t/" $v | expand --initial --tabs=4 > _00_${f}
done

for v in `ls write_*.py | sort`
do
echo $v
python $v
done
for v in `ls *_combine.yaml | sort`
do
echo $v
python combine_MarkMedia.py $v
done
