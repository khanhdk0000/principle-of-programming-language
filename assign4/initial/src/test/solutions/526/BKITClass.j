.source BKITClass.java
.class public BKITClass
.super java.lang.Object
.field static a I
.field static b Ljava/lang/String;
.field static c F

.method public static main([Ljava/lang/String;)V
	iconst_5
	putstatic BKITClass/a I
	ldc "string"
	putstatic BKITClass/b Ljava/lang/String;
	ldc 5.6
	putstatic BKITClass/c F
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic BKITClass/a I
	iconst_5
	if_icmplt Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	getstatic BKITClass/a I
	bipush 10
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	iand
	ifle Label8
Label9:
	bipush 6
	putstatic BKITClass/a I
Label10:
	goto Label2
Label8:
	getstatic BKITClass/a I
	bipush 7
	if_icmpne Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label13
Label15:
	bipush 7
	putstatic BKITClass/a I
Label16:
	goto Label2
Label14:
	goto Label14
Label13:
	bipush 10
	putstatic BKITClass/a I
Label2:
Label14:
	getstatic BKITClass/a I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 7
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LBKITClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
