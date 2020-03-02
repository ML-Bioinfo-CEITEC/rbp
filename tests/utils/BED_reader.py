# Import requests module and gzip.
from requests import get
from gzip import decompress

# The function will download the compressed (gz) BED file,
# and it will decompress it to text.
def bed_reader(target_url, output_name):
  def get_gzipped_bed_(target_url):
    downloaded_bed = get(target_url).content
    decompressed_bed = decompress(downloaded_bed)
    return decompressed_bed
  # Decode from URL to utf-8.
  decompressed = get_gzipped_bed_(target_url)
  bed_file_human_readable = decompressed.decode()
  # Write bed file to new file.
  output_file = open(output_name, "w")
  output_file.write(bed_file_human_readable)
  output_file.close()
  return output_name

bed_reader(url, output_name)

import os
os.path.exists(output_name)
