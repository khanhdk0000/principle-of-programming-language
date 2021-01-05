.source BKITClass.java
.class public BKITClass
.super java.lang.Object
.field static a I
.field static b I
.field static c I

.method public static main([Ljava/lang/String;)V
	iconst_1
	putstatic BKITClass/a I
	iconst_2
	putstatic BKITClass/b I
	iconst_3
	putstatic BKITClass/c I
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
Label0:
	bipush 15
	istore_1
	iconst_1
	putstatic BKITClass/c I
Label4:
	getstatic BKITClass/c I
	iconst_5
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	ldc "start:"
	invokestatic io/print(Ljava/lang/String;)V
	getstatic BKITClass/c I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	getstatic BKITClass/c I
	iconst_1
	isub
	putstatic BKITClass/b I
Label11:
	getstatic BKITClass/b I
	iconst_1
	ineg
	if_icmplt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
Label14:
	getstatic BKITClass/b I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label15:
Label9:
	iconst_1
	ineg
	getstatic BKITClass/b I
	iadd
	putstatic BKITClass/b I
	goto Label11
Label10:
Label8:
Label2:
	iconst_1
	getstatic BKITClass/c I
	iadd
	putstatic BKITClass/c I
	goto Label4
Label3:
Label1:
	return
.limit stack 6
.limit locals 2
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
