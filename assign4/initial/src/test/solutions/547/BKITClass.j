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
.var 1 is x I from Label0 to Label1
.var 2 is y I from Label0 to Label1
.var 3 is z I from Label0 to Label1
Label0:
	iconst_5
	istore_1
	bipush 6
	istore_2
	bipush 7
	istore_3
Label2:
	iload_2
	iload_3
	iadd
	iload_1
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
Label6:
	iload_2
	iload_3
	iadd
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_2
	getstatic BKITClass/a I
	isub
	istore_2
	iload_3
	getstatic BKITClass/a I
	isub
	istore_3
Label7:
	goto Label2
Label3:
	ldc "?"
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 4
.limit locals 4
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
