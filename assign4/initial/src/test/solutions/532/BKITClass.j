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
Label0:
	getstatic BKITClass/b I
	invokestatic BKITClass/f1(I)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static f1(I)V
.var 0 is a I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	if_icmple Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label6
Label7:
	ldc "yes"
	invokestatic io/print(Ljava/lang/String;)V
Label8:
	goto Label2
Label6:
Label2:
Label6:
	return
Label1:
	return
.limit stack 3
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
