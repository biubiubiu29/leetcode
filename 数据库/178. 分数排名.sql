select s1.Score,(select count(distinct s2.Score) from Scores s2 where s2.Score>=s1.Score) Rank
from Scores s1
order by s1.Score desc

--分数排名。如果两个分数相同，则两个分数排名（Rank）相同。请注意，平分后的下一个名次应该是下一个连续的整数值。换句话说，名次之间不应该有“间隔”。
--思路是查询表中有多少个大于或等于当前分数的不重复分数，则该值即为最终的Rank
--distinct实现名次连续