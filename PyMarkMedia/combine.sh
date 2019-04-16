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
