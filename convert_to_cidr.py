# 引入 ipaddress 模塊，用於處理 IP 地址和子網掩碼
import ipaddress

# 將 IP 地址和子網掩碼轉換為 CIDR 表示
def convert_to_cidr(ip, mask):
    # 使用 IP 地址和子網掩碼創建一個 IPv4Network 對象
    # strict=False 表示即使子網掩碼不符合標準也接受
    net = ipaddress.IPv4Network(ip + '/' + mask, strict=False)
    # 返回 CIDR 表示的字符串
    return str(net)

# 將包含 IP 地址和子網掩碼的輸入文件轉換為包含 CIDR 表示的輸出文件
def convert_file(input_file, output_file):
    # 打開輸入文件和輸出文件
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        # 讀取輸入文件的每一行
        for line in f_in:
            # 將每一行的 IP 地址和子網掩碼分開
            ip, mask = line.strip().split()
            # 轉換為 CIDR 表示
            cidr = convert_to_cidr(ip, mask)
            # 將 CIDR 表示寫入輸出文件
            f_out.write(cidr + '\n')

# 這裡的檔名請換成你的檔名
convert_file('mudfish_rules.txt', 'netch_rules.txt')