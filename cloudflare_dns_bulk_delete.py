import requests
import json

# ========== | Fill These Out | ==========
dns_zone_id = ""
cf_api_key = ""
cf_email = ""
# ========================================

list_dns_records_url_template = "https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
delete_dns_record_url_template = "https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{dns_record_id}"

list_dns_records_url = list_dns_records_url_template.replace('{zone_id}', dns_zone_id)
delete_dns_record_url = delete_dns_record_url_template.replace('{zone_id}', dns_zone_id)

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + cf_api_key,
    "X-Auth-Email": cf_email
}

response = requests.request("GET", list_dns_records_url, headers=headers)

if(response.status_code == 200):
    results = json.loads(response.text)["result"]
    record_ids = [item['id'] for item in results if 'id' in item]

    for record_id in record_ids:
        temp_url = delete_dns_record_url.replace("{dns_record_id}", record_id)
        response = requests.request("DELETE", temp_url, headers=headers)
        print(response.text)
else:
    print('\033[91m' + response.text + '\033[0m')