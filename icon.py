import wx
import cStringIO

def GetData():
    return \
'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x02\x00\x00d\x00d\x00\x00\xff\xec\
\x00\x11Ducky\x00\x01\x00\x04\x00\x00\x00d\x00\x00\xff\xee\x00\x0eAdobe\
\x00d\xc0\x00\x00\x00\x01\xff\xdb\x00\x84\x00\x01\x01\x01\x01\x01\x01\
\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\
\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\
\x01\x01\x01\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x03\x03\x03\
\x03\x03\x03\x03\x03\x03\x03\x01\x01\x01\x01\x01\x01\x01\x02\x01\x01\
\x02\x02\x02\x01\x02\x02\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\
\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\xff\xc0\x00\x11\x08\x00\x10\x00\x10\x03\x01\x11\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x01\xa2\x00\x00\x00\x06\x02\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x08\x06\x05\x04\t\x03\n\x02\x01\x00\x0b\x01\x00\x00\x06\x03\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x05\x04\x03\x07\x02\x08\x01\t\x00\n\x0b\x10\x00\x02\x01\x03\x04\x01\x03\x03\x02\x03\x03\x03\x02\x06\tu\x01\x02\x03\x04\x11\x05\x12\x06!\x07\x13"\x00\x081\x14A2#\x15\tQB\x16a$3\x17Rq\x81\x18b\x91%C\xa1\xb1\xf0&4r\n\x19\xc1\xd15\'\xe1S6\x82\xf1\x92\xa2DTsEF7Gc(UVW\x1a\xb2\xc2\xd2\xe2\xf2d\x83t\x93\x84e\xa3\xb3\xc3\xd3\xe3)8f\xf3u*9:HIJXYZghijvwxyz\x85\x86\x87\x88\x89\x8a\x94\x95\x96\x97\x98\x99\x9a\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb4\xb5\xb6\xb7\xb8\xb9\xba\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd4\xd5\xd6\xd7\xd8\xd9\xda\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf4\xf5\xf6\xf7\xf8\xf9\xfa\x11\x00\x02\x01\x03\x02\x04\x04\x03\x05\x04\x04\x04\x06\x06\x05m\x01\x02\x03\x11\x04!\x12\x051\x06\x00"\x13AQ\x072a\x14q\x08B\x81#\x91\x15R\xa1b\x163\t\xb1$\xc1\xd1Cr\xf0\x17\xe1\x824%\x92S\x18cD\xf1\xa2\xb2&5\x19T6Ed\'\ns\x83\x93Ft\xc2\xd2\xe2\xf2UeuV7\x84\x85\xa3\xb3\xc3\xd3\xe3\xf3)\x1a\x94\xa4\xb4\xc4\xd4\xe4\xf4\x95\xa5\xb5\xc5\xd5\xe5\xf5(GWf8v\x86\x96\xa6\xb6\xc6\xd6\xe6\xf6gw\x87\x97\xa7\xb7\xc7\xd7\xe7\xf7HXhx\x88\x98\xa8\xb8\xc8\xd8\xe8\xf89IYiy\x89\x99\xa9\xb9\xc9\xd9\xe9\xf9*:JZjz\x8a\x9a\xaa\xba\xca\xda\xea\xfa\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00?\x00\x1f\xbe\t\xf4\xff\x00\xc7\xce\xf6\xe9\x1e\xd2\xcan.\xb5\xeb\x04\xcc\xfc~\xf8\x95Q\xdb\xd5u\xaf\xd5\xfb\x07)_\xb9\xb3;?h\xc1QU\x1e\xe0\xaf\xc9\xe0\xe7\xac\x9c\xe4\xea\xa9\x99\xea*5\x99\xdd\xdd\x98\xb1bO\xbcE\xe4\xbd\x9f`\xdevY\xa5\xb8\xb6\xb5\xf1\xac\xb6\xbf\x1c\x9f\x06&.\xc9\x18\'Q*I\xa9\x19<O_D\xff\x00y\x9fq\xfd\xdb\xf6\xdb\xdc\xed\xb2\xc3h\xdf7\xcf\xdd\xdc\xcb\xcfglD\x1b\x95\xf4Io\r\xcd\xdb*x\t\x1c\xca\x8a#V\x024\xa0E\x00\x00\x00\x14\xeaW{t\xf7\xc6\xfe\xb3\xf8\x9f\xdf5\xbd\xbf\xd6\x1b?\xa3\xfeQ\xc1\xb7\xab\xe2\xea\x8e\x9e\xcdtV\xdf\xdb\x1b\x97p\xed\xdc\xd5\r=\x04[\xf6\x86\xb6M\x9f\x05~&\x1cl\xcb\x97jj\xc5\xa8\x81E^,"7\x94\xa8ko\x9b?/m\xfc\xaf}&\xe5k\r\x9f0\x88\x9b\xc1\x85\xad\x91\x1d\x95\x96\x82@t\x02\xb4:\xe8\xd5\x1d\xc9A\x9e\x99\xf6\xb3\xdc\x7fx\xf9\xc3\xdf^U\xb5\xe4\x9d\xf7s\xe6?g\x1e\xfa\x1f\xde[\x9c[\xd5\xc5\xc5\xbc3E)sd\xe9\xf5L\x92\x99\x14\xdb\t"(\xe4\xc5pK\r\x15"\xbe\xb7\xaf\xc8O\x8f\xfb\x7f\xa3\xfa\x0fn\xfcQ\xa9\xee.\x96\xed*\xde\x9a\xcbu\xe7\xcc\xcc\x8b\xf6\x1ec\r\xb4\xfb\x9a\xa7\'\x8a\xdapGCC\x8f\xa1\xec\xed\xc1\xf7\xfbZ\xb2xs\t\x90\xc7TPb\xa8e\x8aZph\xd8\x87\x08\x0b\x9b\x7f\xd8`\xd9,m\xf9u\xee-7\x13fb\xbe>)T\x9c\x95A@\x04\xadT\'^\xa5*\x8aA^\xde4\xc9\xcd\xb3\xda?vwos\xf9\xabw\xf7\x9a\xdfg\xe6\x1eKNc[\xeeVA\xb7\xa4\xb7\x1bZ\xa4\xd7M\xad\xa4m\xbe\x1d\x17\n\xa6\xd4\xc1<s\\\xca\xac\xb2\x118\x05u<n_\x93}\x0b\xda\x7f\x13\xfb\xae\x83\xe4Mgt\xf7W\xceL\xa6C\x0f\x8f\xe9\x0e\xef\xdd\xdd\x9d\xb9\xf7\x96\x03g\xf5\xa5\x0eOj\xd7\xe5v~X\xe7\xbbh4\xdfsL\xdb\x94SBv\xfeI\x12\xa3(\x8c\xb2\xc6\xc4\xbc.^s&\xc5\xb9r\xc5\xec{\xdb\xdc\xdd\xf3{P[\xce\xf34\x8a\x91\x02\x84\xa1\xd56k\xfa\xb4\x1e\x1be\xc5\x08\xe2\x10r\xe7\xb2\xbe\xea\xf2_\xbe\xbc\xb5y\xed\x85\xb6\xc9\xcb\xdfwX5I\xbb\xedV\xdbl6\xb3\\\xdf2\xce\x91\xddG\xe0\xed\x94P\xa7\xe8\x0c\x8f\xf5\xb0\x12\x96\xec\x19\x18\r2\x7f\xff\xd9'


def GetBitmap():
    return wx.BitmapFromImage(GetImage())


def GetImage():
    stream = cStringIO.StringIO(GetData())
    return wx.ImageFromStream(stream)


def GetIcon():
    icon = wx.EmptyIcon()
    icon.CopyFromBitmap(GetBitmap())
    return icon




