# NBA-player-classification-ML
Classification of NBA players into 5 positions on the basketball court: SG (shooting guard), PG (point guard), SF (small forward), PF (power forward), and C (center) based on the players' per-game average performance in the 2015-2016 season.
## Running Instructions
python NBA-Classification
## Example Output
['Player', 'Pos', 'Age', 'Tm', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PS/G']
         Player Pos  Age   Tm   G  GS    MP   FG  FGA    FG%  ...    FT%  ORB  \
0    Quincy Acy  PF   25  SAC  59  29  14.8  2.0  3.6  0.556  ...  0.735  1.1   
1  Jordan Adams  SG   21  MEM   2   0   7.5  1.0  3.0  0.333  ...  0.600  0.0   
2  Steven Adams   C   22  OKC  80  80  25.2  3.3  5.3  0.613  ...  0.582  2.7   

   DRB  TRB  AST  STL  BLK  TOV   PF  PS/G  
0  2.1  3.2  0.5  0.5  0.4  0.5  1.7   5.2  
1  1.0  1.0  1.5  1.5  0.0  1.0  1.0   3.5  
2  3.9  6.7  0.8  0.5  1.1  1.1  2.8   8.0  

[3 rows x 29 columns]
   Age   G  GS    MP   FG  FGA    FG%   3P  3PA    3P%  ...    FT%  ORB  DRB  \
0   25  59  29  14.8  2.0  3.6  0.556  0.3  0.8  0.388  ...  0.735  1.1  2.1   
1   21   2   0   7.5  1.0  3.0  0.333  0.0  0.5  0.000  ...  0.600  0.0  1.0   
2   22  80  80  25.2  3.3  5.3  0.613  0.0  0.0  0.000  ...  0.582  2.7  3.9   

   TRB  AST  STL  BLK  TOV   PF  PS/G  
0  3.2  0.5  0.5  0.4  0.5  1.7   5.2  
1  1.0  1.5  1.5  0.0  1.0  1.0   3.5  
2  6.7  0.8  0.5  1.1  1.1  2.8   8.0  

[3 rows x 26 columns]
['PF', 'SG', 'C']
Test set predictions:
['C' 'C' 'SF' 'SG' 'PF' 'SG' 'C' 'PG' 'SG' 'PF' 'SG' 'SF' 'C' 'PF' 'SG'
 'SG' 'PF' 'PG' 'SF' 'PG' 'C' 'PF' 'PG' 'C' 'C' 'PG' 'SG' 'SF' 'SF' 'C'
 'PF' 'PF' 'C' 'PF' 'C' 'PG' 'PF' 'PF' 'PG' 'SF' 'C' 'PF' 'PG' 'PG' 'PF'
 'PF' 'SF' 'PF' 'SF' 'C' 'PG' 'SF' 'C' 'C' 'SF' 'SF' 'SG' 'PF' 'PF' 'C'
 'SF' 'PF' 'SF' 'SG' 'C' 'SF' 'C' 'C' 'C' 'C' 'C' 'C' 'SF' 'SG' 'PF' 'SG'
 'SF' 'SG' 'PG' 'SF' 'SG' 'SF' 'PF' 'PF' 'C' 'PF' 'SF' 'C' 'C' 'SG' 'C'
 'SF' 'PF' 'SF' 'PG' 'PF' 'C' 'PG' 'PF' 'SF' 'SF' 'SF' 'PF' 'PG' 'C' 'PG'
 'PG' 'C' 'SF' 'PG' 'SF' 'PF' 'C' 'C' 'C' 'SG' 'SG' 'SF' 'SF']
Test set accuracy: 0.57
