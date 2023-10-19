import os
from datetime import datetime,timedelta,time
import stat, time
from operator import itemgetter


def action_done(self):
    current_date = datetime.now().strftime('%Y-%m-%d')
    folder_path = 'E:\\py\\{0}\\{1}\\{2}'.format(current_date[:4],current_date[5:7],current_date[8:10])
# doc file trong trong 10p
    time_threshold = datetime.now() -timedelta(minutes=10)
    file_bf_10m = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            modified_time = datetime.fromtimestamp(os.path.getatime(file_path))       
            # So sánh thời gian sửa đổi với ngưỡng thời gian
            if modified_time >= time_threshold:
                file_bf_10m.append(file_name)
    print(file_bf_10m)
    # doc file ko lap
    folder = file_bf_10m
    file_no_repeat = []
    seen = set()
    for item in folder:
        name_item = item.split('_')
        if name_item[3] not in seen:
            file_no_repeat.append(name_item)
            seen.add(name_item[3])
        day  = datetime.strptime(file_names[4][0:8], "%Y%m%d").date(),
        time = datetime.strptime(file_names[4][8:14], "%H%M%S").time(),
    
    print("_______________")
    print(file_no_repeat)
    
    #   ghi file vao cac truong          
    for file_names in file_no_repeat:
        new_record = self.env['department'].create({
                    'TKTHs': file_names[0],
                    'TNs': file_names[1],
                    'stt': file_names[2],
                    'maXe': file_names[3],
                    'day': datetime.strptime(file_names[4][0:8], "%Y%m%d").date(),
                    'time': datetime.strptime(file_names[4][8:14], "%H%M%S").time(),
            
        })
    
        
        
# last_time =datetime.datetime.strptime('000010', "%H%M%S").time()
# last_day = datetime.datetime.strptime('20000101',"%Y%m%d").date()
    
  
def tach_file():
    folder_paths = 'E:\py'

    for root, _, files in os.walk(folder_paths):
        for file in files:
            file_path = os.path.join(root, file)
            print(file)
            
            # file_stat = os.stat(file_path)
            # created_time = datetime.fromtimestamp(file_stat.st_mtime)
            
            # file_parts = file_path.split('_')
            # TKTHs = file_parts[0]
            # TNs   = file_parts[1]
            # stt  = file_parts[2]
            # maXe = file_parts[3]
            # gio2 = datetime.strptime(file_parts[4][8:14], "%H%M%S").time()
            # day = datetime.strptime(file_parts[4][:8],"%Y%m%d").date()

        
            # lay gio cuoi cung va ngay







# def get_latest_created_files(folder_path):
#     files_and_times = []
    

#     for root, _, files in os.walk(folder_path):
#         for file in files:
#             file_path = os.path.join(root, file)
#             file_stat = os.stat(file_path)
#             created_time = datetime.datetime.fromtimestamp(file_stat.st_ctime)
#             files_and_times.append((file_path, created_time))

#     if not files_and_times:
#         return None

#     # Sắp xếp danh sách các tệp theo thời gian tạo tăng dần
#     files_and_times.sort(key=lambda x: x[1])

#     return files_and_times

# folder_path = r'E:\py\2023\09\22'
# latest_created_files = get_latest_created_files(folder_path)
# print(len(latest_created_files))
# if latest_created_files:
#     print("Các tệp theo thời gian tạo tăng dần:")
#     for file_path, created_time in latest_created_files:
#         print(f"Tệp: {file_path}, Thời gian tạo: {created_time}")
# else:
#     print("Không có tệp trong thư mục.")






import os
from datetime import datetime, timedelta
from operator import itemgetter
latest_time = datetime.datetime.strptime(latest_time, "%Y-%m-%d %H:%M:%S")
     
def read_folder(latest_time):
    latest_time = latest_time = datetime.datetime.strptime(latest_time, "%Y-%m-%d")
    latest_time = datetime(2023, 9, 23)
    files_and_times = []
    today = datetime.now()

    date_range = [latest_time + timedelta(days=x) for x in range((today - latest_time).days + 1)]


    # Lặp qua từng ngày trong danh sách và đọc tệp tin tương ứng (nếu có)
    for date in date_range:
        folder_path = os.path.join(
            'E:\py', date.strftime('%Y'), date.strftime('%m'), date.strftime('%d'))
        
        if os.path.exists(folder_path):  # Kiểm tra xem thư mục tồn tại trước khi đọc
            for root, _, files in os.walk(folder_path):
                for file in files:
    
                    file_path = os.path.join(root, file)
                    file_stat = os.stat(file_path)
                    created_time = datetime.fromtimestamp(file_stat.st_ctime)
                    created_time = created_time.replace(microsecond=0)
                    files_and_times.append((file, created_time))
        else:
            print(f"Thư mục {folder_path} không tồn tại ({date.strftime('%d/%m/%Y')})")


    # Sắp xếp danh sách các tệp theo thời gian tạo tăng dần
    files_and_times.sort(key=itemgetter(1))
    return  files_and_times

    
read_folder()

