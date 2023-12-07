import csv

with open('NBA Player Stats Dataset for the 2022-2023 _exported.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    three_mean=0
    ft_mean=0;
    two_mean=0
    two_min=1000
    three_min=1000
    ft_min=1000
    ft_max=0
    three_max=0
    two_max=0
    for row in csv_reader:
        if line_count == 0:
            col_num=0
            for col in row:
                print(col_num)
                print(col)
                col_num+=1
            line_count += 1
        else:
            two_current=float(row[14])
            three_current=float(row[11])
            ft_current=float(row[18])
            two_mean+=two_current
            three_mean+=three_current
            ft_mean=ft_current
            if two_current>two_max:
                two_max=two_current
            if three_current>three_max:
                three_max=three_current
            if ft_current>ft_max:
                ft_max=ft_current
            if two_current<two_min:
                if two_current>0:
                    two_min=two_current
            if three_current<three_min:
                if three_current>0:
                    three_min=three_current
            if ft_current<ft_min:
                if ft_current>0:
                    ft_min=ft_current
            line_count+=1
    three_mean=three_mean/(line_count-1)
    two_mean=two_mean/(line_count-1)
    ft_mean=ft_mean/(line_count-1)
    print('3pt avg: ', three_mean, '2pt avg: ', two_mean, 'ft avg: ', ft_mean)
    print('3pt max: ', three_max, '2pt max: ', two_max, 'ft max: ', ft_max)
    print('3pt min: ', three_min, '2pt min: ', two_min, 'ft min: ', ft_min)