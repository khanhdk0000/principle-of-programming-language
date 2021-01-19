# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u0207\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2")
        buf.write("\3\2\7\2\u009a\n\2\f\2\16\2\u009d\13\2\3\3\3\3\3\4\6\4")
        buf.write("\u00a2\n\4\r\4\16\4\u00a3\3\4\3\4\3\5\3\5\3\5\3\5\7\5")
        buf.write("\u00ac\n\5\f\5\16\5\u00af\13\5\3\5\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3%\3")
        buf.write("%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3+\3+\3")
        buf.write("+\3,\3,\3,\3-\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3")
        buf.write(";\3<\3<\3<\7<\u018f\n<\f<\16<\u0192\13<\5<\u0194\n<\3")
        buf.write("=\3=\3=\3=\7=\u019a\n=\f=\16=\u019d\13=\3>\3>\3>\3>\7")
        buf.write(">\u01a3\n>\f>\16>\u01a6\13>\3?\3?\3?\5?\u01ab\n?\3@\6")
        buf.write("@\u01ae\n@\r@\16@\u01af\3A\3A\7A\u01b4\nA\fA\16A\u01b7")
        buf.write("\13A\3B\3B\5B\u01bb\nB\3B\6B\u01be\nB\rB\16B\u01bf\3C")
        buf.write("\3C\3C\3C\3C\3C\3C\5C\u01c9\nC\5C\u01cb\nC\3D\3D\3D\3")
        buf.write("E\3E\3E\3E\5E\u01d4\nE\3F\3F\7F\u01d8\nF\fF\16F\u01db")
        buf.write("\13F\3F\3F\3F\3G\3G\3G\3G\3G\5G\u01e5\nG\3H\3H\3I\3I\7")
        buf.write("I\u01eb\nI\fI\16I\u01ee\13I\3I\5I\u01f1\nI\3I\3I\3J\3")
        buf.write("J\7J\u01f7\nJ\fJ\16J\u01fa\13J\3J\3J\3J\3K\3K\3K\3K\7")
        buf.write("K\u0203\nK\fK\16K\u0206\13K\4\u00ad\u0204\2L\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w\2y\2{")
        buf.write("\2}=\177\2\u0081\2\u0083\2\u0085>\u0087\2\u0089\2\u008b")
        buf.write("?\u008d\2\u008f@\u0091A\u0093B\u0095C\3\2\24\3\2c|\6\2")
        buf.write("\62;C\\aac|\5\2\13\f\17\17\"\"\3\2\63;\3\2\62;\4\2ZZz")
        buf.write("z\4\2\63;CH\4\2\62;CH\4\2QQqq\3\2\639\3\2\629\4\2GGgg")
        buf.write("\4\2--//\t\2))^^ddhhppttvv\7\2\f\f\16\17$$))^^\3\2^^\3")
        buf.write("\2$$\4\3\f\f\16\17\2\u0214\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2}\3\2\2\2\2\u0085\3\2\2\2\2\u008b\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\3\u0097\3\2\2\2\5\u009e\3\2\2\2\7\u00a1\3\2\2\2\t\u00a7")
        buf.write("\3\2\2\2\13\u00b5\3\2\2\2\r\u00ba\3\2\2\2\17\u00c0\3\2")
        buf.write("\2\2\21\u00c9\3\2\2\2\23\u00cc\3\2\2\2\25\u00d1\3\2\2")
        buf.write("\2\27\u00d8\3\2\2\2\31\u00e0\3\2\2\2\33\u00e6\3\2\2\2")
        buf.write("\35\u00ed\3\2\2\2\37\u00f6\3\2\2\2!\u00fa\3\2\2\2#\u0103")
        buf.write("\3\2\2\2%\u0106\3\2\2\2\'\u0110\3\2\2\2)\u0117\3\2\2\2")
        buf.write("+\u011c\3\2\2\2-\u0120\3\2\2\2/\u0126\3\2\2\2\61\u012c")
        buf.write("\3\2\2\2\63\u0131\3\2\2\2\65\u0137\3\2\2\2\67\u0139\3")
        buf.write("\2\2\29\u013c\3\2\2\2;\u013e\3\2\2\2=\u0141\3\2\2\2?\u0143")
        buf.write("\3\2\2\2A\u0146\3\2\2\2C\u0148\3\2\2\2E\u014b\3\2\2\2")
        buf.write("G\u014d\3\2\2\2I\u014f\3\2\2\2K\u0152\3\2\2\2M\u0155\3")
        buf.write("\2\2\2O\u0158\3\2\2\2Q\u015b\3\2\2\2S\u015d\3\2\2\2U\u015f")
        buf.write("\3\2\2\2W\u0162\3\2\2\2Y\u0165\3\2\2\2[\u0169\3\2\2\2")
        buf.write("]\u016c\3\2\2\2_\u016f\3\2\2\2a\u0173\3\2\2\2c\u0177\3")
        buf.write("\2\2\2e\u0179\3\2\2\2g\u017b\3\2\2\2i\u017d\3\2\2\2k\u017f")
        buf.write("\3\2\2\2m\u0181\3\2\2\2o\u0183\3\2\2\2q\u0185\3\2\2\2")
        buf.write("s\u0187\3\2\2\2u\u0189\3\2\2\2w\u0193\3\2\2\2y\u0195\3")
        buf.write("\2\2\2{\u019e\3\2\2\2}\u01aa\3\2\2\2\177\u01ad\3\2\2\2")
        buf.write("\u0081\u01b1\3\2\2\2\u0083\u01b8\3\2\2\2\u0085\u01ca\3")
        buf.write("\2\2\2\u0087\u01cc\3\2\2\2\u0089\u01d3\3\2\2\2\u008b\u01d5")
        buf.write("\3\2\2\2\u008d\u01e4\3\2\2\2\u008f\u01e6\3\2\2\2\u0091")
        buf.write("\u01e8\3\2\2\2\u0093\u01f4\3\2\2\2\u0095\u01fe\3\2\2\2")
        buf.write("\u0097\u009b\t\2\2\2\u0098\u009a\t\3\2\2\u0099\u0098\3")
        buf.write("\2\2\2\u009a\u009d\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c")
        buf.write("\3\2\2\2\u009c\4\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u009f")
        buf.write("\7?\2\2\u009f\6\3\2\2\2\u00a0\u00a2\t\4\2\2\u00a1\u00a0")
        buf.write("\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3")
        buf.write("\u00a4\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6\b\4\2\2")
        buf.write("\u00a6\b\3\2\2\2\u00a7\u00a8\7,\2\2\u00a8\u00a9\7,\2\2")
        buf.write("\u00a9\u00ad\3\2\2\2\u00aa\u00ac\13\2\2\2\u00ab\u00aa")
        buf.write("\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ad")
        buf.write("\u00ab\3\2\2\2\u00ae\u00b0\3\2\2\2\u00af\u00ad\3\2\2\2")
        buf.write("\u00b0\u00b1\7,\2\2\u00b1\u00b2\7,\2\2\u00b2\u00b3\3\2")
        buf.write("\2\2\u00b3\u00b4\b\5\2\2\u00b4\n\3\2\2\2\u00b5\u00b6\7")
        buf.write("D\2\2\u00b6\u00b7\7q\2\2\u00b7\u00b8\7f\2\2\u00b8\u00b9")
        buf.write("\7{\2\2\u00b9\f\3\2\2\2\u00ba\u00bb\7D\2\2\u00bb\u00bc")
        buf.write("\7t\2\2\u00bc\u00bd\7g\2\2\u00bd\u00be\7c\2\2\u00be\u00bf")
        buf.write("\7m\2\2\u00bf\16\3\2\2\2\u00c0\u00c1\7E\2\2\u00c1\u00c2")
        buf.write("\7q\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c4\7v\2\2\u00c4\u00c5")
        buf.write("\7k\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7\7w\2\2\u00c7\u00c8")
        buf.write("\7g\2\2\u00c8\20\3\2\2\2\u00c9\u00ca\7F\2\2\u00ca\u00cb")
        buf.write("\7q\2\2\u00cb\22\3\2\2\2\u00cc\u00cd\7G\2\2\u00cd\u00ce")
        buf.write("\7n\2\2\u00ce\u00cf\7u\2\2\u00cf\u00d0\7g\2\2\u00d0\24")
        buf.write("\3\2\2\2\u00d1\u00d2\7G\2\2\u00d2\u00d3\7n\2\2\u00d3\u00d4")
        buf.write("\7u\2\2\u00d4\u00d5\7g\2\2\u00d5\u00d6\7K\2\2\u00d6\u00d7")
        buf.write("\7h\2\2\u00d7\26\3\2\2\2\u00d8\u00d9\7G\2\2\u00d9\u00da")
        buf.write("\7p\2\2\u00da\u00db\7f\2\2\u00db\u00dc\7D\2\2\u00dc\u00dd")
        buf.write("\7q\2\2\u00dd\u00de\7f\2\2\u00de\u00df\7{\2\2\u00df\30")
        buf.write("\3\2\2\2\u00e0\u00e1\7G\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3")
        buf.write("\7f\2\2\u00e3\u00e4\7K\2\2\u00e4\u00e5\7h\2\2\u00e5\32")
        buf.write("\3\2\2\2\u00e6\u00e7\7G\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9")
        buf.write("\7f\2\2\u00e9\u00ea\7H\2\2\u00ea\u00eb\7q\2\2\u00eb\u00ec")
        buf.write("\7t\2\2\u00ec\34\3\2\2\2\u00ed\u00ee\7G\2\2\u00ee\u00ef")
        buf.write("\7p\2\2\u00ef\u00f0\7f\2\2\u00f0\u00f1\7Y\2\2\u00f1\u00f2")
        buf.write("\7j\2\2\u00f2\u00f3\7k\2\2\u00f3\u00f4\7n\2\2\u00f4\u00f5")
        buf.write("\7g\2\2\u00f5\36\3\2\2\2\u00f6\u00f7\7H\2\2\u00f7\u00f8")
        buf.write("\7q\2\2\u00f8\u00f9\7t\2\2\u00f9 \3\2\2\2\u00fa\u00fb")
        buf.write("\7H\2\2\u00fb\u00fc\7w\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe")
        buf.write("\7e\2\2\u00fe\u00ff\7v\2\2\u00ff\u0100\7k\2\2\u0100\u0101")
        buf.write("\7q\2\2\u0101\u0102\7p\2\2\u0102\"\3\2\2\2\u0103\u0104")
        buf.write("\7K\2\2\u0104\u0105\7h\2\2\u0105$\3\2\2\2\u0106\u0107")
        buf.write("\7R\2\2\u0107\u0108\7c\2\2\u0108\u0109\7t\2\2\u0109\u010a")
        buf.write("\7c\2\2\u010a\u010b\7o\2\2\u010b\u010c\7g\2\2\u010c\u010d")
        buf.write("\7v\2\2\u010d\u010e\7g\2\2\u010e\u010f\7t\2\2\u010f&\3")
        buf.write("\2\2\2\u0110\u0111\7T\2\2\u0111\u0112\7g\2\2\u0112\u0113")
        buf.write("\7v\2\2\u0113\u0114\7w\2\2\u0114\u0115\7t\2\2\u0115\u0116")
        buf.write("\7p\2\2\u0116(\3\2\2\2\u0117\u0118\7V\2\2\u0118\u0119")
        buf.write("\7j\2\2\u0119\u011a\7g\2\2\u011a\u011b\7p\2\2\u011b*\3")
        buf.write("\2\2\2\u011c\u011d\7X\2\2\u011d\u011e\7c\2\2\u011e\u011f")
        buf.write("\7t\2\2\u011f,\3\2\2\2\u0120\u0121\7Y\2\2\u0121\u0122")
        buf.write("\7j\2\2\u0122\u0123\7k\2\2\u0123\u0124\7n\2\2\u0124\u0125")
        buf.write("\7g\2\2\u0125.\3\2\2\2\u0126\u0127\7G\2\2\u0127\u0128")
        buf.write("\7p\2\2\u0128\u0129\7f\2\2\u0129\u012a\7F\2\2\u012a\u012b")
        buf.write("\7q\2\2\u012b\60\3\2\2\2\u012c\u012d\7V\2\2\u012d\u012e")
        buf.write("\7t\2\2\u012e\u012f\7w\2\2\u012f\u0130\7g\2\2\u0130\62")
        buf.write("\3\2\2\2\u0131\u0132\7H\2\2\u0132\u0133\7c\2\2\u0133\u0134")
        buf.write("\7n\2\2\u0134\u0135\7u\2\2\u0135\u0136\7g\2\2\u0136\64")
        buf.write("\3\2\2\2\u0137\u0138\7-\2\2\u0138\66\3\2\2\2\u0139\u013a")
        buf.write("\7-\2\2\u013a\u013b\7\60\2\2\u013b8\3\2\2\2\u013c\u013d")
        buf.write("\7/\2\2\u013d:\3\2\2\2\u013e\u013f\7/\2\2\u013f\u0140")
        buf.write("\7\60\2\2\u0140<\3\2\2\2\u0141\u0142\7,\2\2\u0142>\3\2")
        buf.write("\2\2\u0143\u0144\7,\2\2\u0144\u0145\7\60\2\2\u0145@\3")
        buf.write("\2\2\2\u0146\u0147\7^\2\2\u0147B\3\2\2\2\u0148\u0149\7")
        buf.write("^\2\2\u0149\u014a\7\60\2\2\u014aD\3\2\2\2\u014b\u014c")
        buf.write("\7\'\2\2\u014cF\3\2\2\2\u014d\u014e\7#\2\2\u014eH\3\2")
        buf.write("\2\2\u014f\u0150\7(\2\2\u0150\u0151\7(\2\2\u0151J\3\2")
        buf.write("\2\2\u0152\u0153\7~\2\2\u0153\u0154\7~\2\2\u0154L\3\2")
        buf.write("\2\2\u0155\u0156\7?\2\2\u0156\u0157\7?\2\2\u0157N\3\2")
        buf.write("\2\2\u0158\u0159\7#\2\2\u0159\u015a\7?\2\2\u015aP\3\2")
        buf.write("\2\2\u015b\u015c\7>\2\2\u015cR\3\2\2\2\u015d\u015e\7@")
        buf.write("\2\2\u015eT\3\2\2\2\u015f\u0160\7>\2\2\u0160\u0161\7?")
        buf.write("\2\2\u0161V\3\2\2\2\u0162\u0163\7@\2\2\u0163\u0164\7?")
        buf.write("\2\2\u0164X\3\2\2\2\u0165\u0166\7?\2\2\u0166\u0167\7\61")
        buf.write("\2\2\u0167\u0168\7?\2\2\u0168Z\3\2\2\2\u0169\u016a\7>")
        buf.write("\2\2\u016a\u016b\7\60\2\2\u016b\\\3\2\2\2\u016c\u016d")
        buf.write("\7@\2\2\u016d\u016e\7\60\2\2\u016e^\3\2\2\2\u016f\u0170")
        buf.write("\7>\2\2\u0170\u0171\7?\2\2\u0171\u0172\7\60\2\2\u0172")
        buf.write("`\3\2\2\2\u0173\u0174\7@\2\2\u0174\u0175\7?\2\2\u0175")
        buf.write("\u0176\7\60\2\2\u0176b\3\2\2\2\u0177\u0178\7*\2\2\u0178")
        buf.write("d\3\2\2\2\u0179\u017a\7+\2\2\u017af\3\2\2\2\u017b\u017c")
        buf.write("\7]\2\2\u017ch\3\2\2\2\u017d\u017e\7_\2\2\u017ej\3\2\2")
        buf.write("\2\u017f\u0180\7<\2\2\u0180l\3\2\2\2\u0181\u0182\7\60")
        buf.write("\2\2\u0182n\3\2\2\2\u0183\u0184\7.\2\2\u0184p\3\2\2\2")
        buf.write("\u0185\u0186\7=\2\2\u0186r\3\2\2\2\u0187\u0188\7}\2\2")
        buf.write("\u0188t\3\2\2\2\u0189\u018a\7\177\2\2\u018av\3\2\2\2\u018b")
        buf.write("\u0194\7\62\2\2\u018c\u0190\t\5\2\2\u018d\u018f\t\6\2")
        buf.write("\2\u018e\u018d\3\2\2\2\u018f\u0192\3\2\2\2\u0190\u018e")
        buf.write("\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u0194\3\2\2\2\u0192")
        buf.write("\u0190\3\2\2\2\u0193\u018b\3\2\2\2\u0193\u018c\3\2\2\2")
        buf.write("\u0194x\3\2\2\2\u0195\u0196\7\62\2\2\u0196\u0197\t\7\2")
        buf.write("\2\u0197\u019b\t\b\2\2\u0198\u019a\t\t\2\2\u0199\u0198")
        buf.write("\3\2\2\2\u019a\u019d\3\2\2\2\u019b\u0199\3\2\2\2\u019b")
        buf.write("\u019c\3\2\2\2\u019cz\3\2\2\2\u019d\u019b\3\2\2\2\u019e")
        buf.write("\u019f\7\62\2\2\u019f\u01a0\t\n\2\2\u01a0\u01a4\t\13\2")
        buf.write("\2\u01a1\u01a3\t\f\2\2\u01a2\u01a1\3\2\2\2\u01a3\u01a6")
        buf.write("\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5")
        buf.write("|\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a7\u01ab\5w<\2\u01a8")
        buf.write("\u01ab\5y=\2\u01a9\u01ab\5{>\2\u01aa\u01a7\3\2\2\2\u01aa")
        buf.write("\u01a8\3\2\2\2\u01aa\u01a9\3\2\2\2\u01ab~\3\2\2\2\u01ac")
        buf.write("\u01ae\t\6\2\2\u01ad\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2")
        buf.write("\u01af\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u0080\3")
        buf.write("\2\2\2\u01b1\u01b5\7\60\2\2\u01b2\u01b4\t\6\2\2\u01b3")
        buf.write("\u01b2\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5\u01b3\3\2\2\2")
        buf.write("\u01b5\u01b6\3\2\2\2\u01b6\u0082\3\2\2\2\u01b7\u01b5\3")
        buf.write("\2\2\2\u01b8\u01ba\t\r\2\2\u01b9\u01bb\t\16\2\2\u01ba")
        buf.write("\u01b9\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bd\3\2\2\2")
        buf.write("\u01bc\u01be\t\6\2\2\u01bd\u01bc\3\2\2\2\u01be\u01bf\3")
        buf.write("\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u0084")
        buf.write("\3\2\2\2\u01c1\u01c2\5\177@\2\u01c2\u01c3\5\u0081A\2\u01c3")
        buf.write("\u01c4\5\u0083B\2\u01c4\u01cb\3\2\2\2\u01c5\u01c8\5\177")
        buf.write("@\2\u01c6\u01c9\5\u0081A\2\u01c7\u01c9\5\u0083B\2\u01c8")
        buf.write("\u01c6\3\2\2\2\u01c8\u01c7\3\2\2\2\u01c9\u01cb\3\2\2\2")
        buf.write("\u01ca\u01c1\3\2\2\2\u01ca\u01c5\3\2\2\2\u01cb\u0086\3")
        buf.write("\2\2\2\u01cc\u01cd\7^\2\2\u01cd\u01ce\t\17\2\2\u01ce\u0088")
        buf.write("\3\2\2\2\u01cf\u01d4\n\20\2\2\u01d0\u01d4\5\u0087D\2\u01d1")
        buf.write("\u01d2\7)\2\2\u01d2\u01d4\7$\2\2\u01d3\u01cf\3\2\2\2\u01d3")
        buf.write("\u01d0\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d4\u008a\3\2\2\2")
        buf.write("\u01d5\u01d9\7$\2\2\u01d6\u01d8\5\u0089E\2\u01d7\u01d6")
        buf.write("\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9\u01d7\3\2\2\2\u01d9")
        buf.write("\u01da\3\2\2\2\u01da\u01dc\3\2\2\2\u01db\u01d9\3\2\2\2")
        buf.write("\u01dc\u01dd\7$\2\2\u01dd\u01de\bF\3\2\u01de\u008c\3\2")
        buf.write("\2\2\u01df\u01e0\7^\2\2\u01e0\u01e5\n\17\2\2\u01e1\u01e5")
        buf.write("\n\21\2\2\u01e2\u01e3\7)\2\2\u01e3\u01e5\n\22\2\2\u01e4")
        buf.write("\u01df\3\2\2\2\u01e4\u01e1\3\2\2\2\u01e4\u01e2\3\2\2\2")
        buf.write("\u01e5\u008e\3\2\2\2\u01e6\u01e7\13\2\2\2\u01e7\u0090")
        buf.write("\3\2\2\2\u01e8\u01ec\7$\2\2\u01e9\u01eb\5\u0089E\2\u01ea")
        buf.write("\u01e9\3\2\2\2\u01eb\u01ee\3\2\2\2\u01ec\u01ea\3\2\2\2")
        buf.write("\u01ec\u01ed\3\2\2\2\u01ed\u01f0\3\2\2\2\u01ee\u01ec\3")
        buf.write("\2\2\2\u01ef\u01f1\t\23\2\2\u01f0\u01ef\3\2\2\2\u01f1")
        buf.write("\u01f2\3\2\2\2\u01f2\u01f3\bI\4\2\u01f3\u0092\3\2\2\2")
        buf.write("\u01f4\u01f8\7$\2\2\u01f5\u01f7\5\u0089E\2\u01f6\u01f5")
        buf.write("\3\2\2\2\u01f7\u01fa\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f8")
        buf.write("\u01f9\3\2\2\2\u01f9\u01fb\3\2\2\2\u01fa\u01f8\3\2\2\2")
        buf.write("\u01fb\u01fc\5\u008dG\2\u01fc\u01fd\bJ\5\2\u01fd\u0094")
        buf.write("\3\2\2\2\u01fe\u01ff\7,\2\2\u01ff\u0200\7,\2\2\u0200\u0204")
        buf.write("\3\2\2\2\u0201\u0203\13\2\2\2\u0202\u0201\3\2\2\2\u0203")
        buf.write("\u0206\3\2\2\2\u0204\u0205\3\2\2\2\u0204\u0202\3\2\2\2")
        buf.write("\u0205\u0096\3\2\2\2\u0206\u0204\3\2\2\2\30\2\u009b\u00a3")
        buf.write("\u00ad\u0190\u0193\u019b\u01a4\u01aa\u01af\u01b5\u01ba")
        buf.write("\u01bf\u01c8\u01ca\u01d3\u01d9\u01e4\u01ec\u01f0\u01f8")
        buf.write("\u0204\6\b\2\2\3F\2\3I\3\3J\4")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    ASSIGN = 2
    WS = 3
    COMMENT = 4
    BODY = 5
    BREAK = 6
    CONTINUE = 7
    DO = 8
    ELSE = 9
    ELSEIF = 10
    ENDBODY = 11
    ENDIF = 12
    ENDFOR = 13
    ENDWHILE = 14
    FOR = 15
    FUNCTION = 16
    IF = 17
    PARAMETER = 18
    RETURN = 19
    THEN = 20
    VAR = 21
    WHILE = 22
    ENDDO = 23
    TRUE = 24
    FALSE = 25
    ADD = 26
    ADDF = 27
    SUB = 28
    SUBF = 29
    MUL = 30
    MULF = 31
    DIV = 32
    DIVF = 33
    MOD = 34
    NEGATE = 35
    AND = 36
    OR = 37
    EQ = 38
    NOTEQ = 39
    LT = 40
    GT = 41
    LTE = 42
    GTE = 43
    NOTEQF = 44
    LTF = 45
    GTF = 46
    LTEF = 47
    GTEF = 48
    LP = 49
    RP = 50
    LS = 51
    RS = 52
    COLON = 53
    DOT = 54
    COMMA = 55
    SEMI = 56
    LB = 57
    RB = 58
    INTLIT = 59
    FLOATLIT = 60
    STRINGLIT = 61
    ERROR_CHAR = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64
    UNTERMINATED_COMMENT = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", 
            "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", 
            "'For'", "'Function'", "'If'", "'Parameter'", "'Return'", "'Then'", 
            "'Var'", "'While'", "'EndDo'", "'True'", "'False'", "'+'", "'+.'", 
            "'-'", "'-.'", "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", 
            "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
            "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", "'('", "')'", "'['", 
            "']'", "':'", "'.'", "','", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "ASSIGN", "WS", "COMMENT", "BODY", "BREAK", "CONTINUE", 
            "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", 
            "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", "VAR", 
            "WHILE", "ENDDO", "TRUE", "FALSE", "ADD", "ADDF", "SUB", "SUBF", 
            "MUL", "MULF", "DIV", "DIVF", "MOD", "NEGATE", "AND", "OR", 
            "EQ", "NOTEQ", "LT", "GT", "LTE", "GTE", "NOTEQF", "LTF", "GTF", 
            "LTEF", "GTEF", "LP", "RP", "LS", "RS", "COLON", "DOT", "COMMA", 
            "SEMI", "LB", "RB", "INTLIT", "FLOATLIT", "STRINGLIT", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "ID", "ASSIGN", "WS", "COMMENT", "BODY", "BREAK", "CONTINUE", 
                  "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", 
                  "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", 
                  "THEN", "VAR", "WHILE", "ENDDO", "TRUE", "FALSE", "ADD", 
                  "ADDF", "SUB", "SUBF", "MUL", "MULF", "DIV", "DIVF", "MOD", 
                  "NEGATE", "AND", "OR", "EQ", "NOTEQ", "LT", "GT", "LTE", 
                  "GTE", "NOTEQF", "LTF", "GTF", "LTEF", "GTEF", "LP", "RP", 
                  "LS", "RS", "COLON", "DOT", "COMMA", "SEMI", "LB", "RB", 
                  "DECIMAL", "HEXIMAL", "OCTAL", "INTLIT", "INT_PART", "DEC_PART", 
                  "EXPONENT", "FLOATLIT", "ESC_SEQ", "STRING_ESC_SEQUENCE", 
                  "STRINGLIT", "ESC_ILLEGAL", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[68] = self.STRINGLIT_action 
            actions[71] = self.UNCLOSE_STRING_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		self.text = (self.text)[1:-1]
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    self.text = (self.text)[1:]
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    self.text = (self.text)[1:]
                
     


