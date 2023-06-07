using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace ChatWebApp.Migrations
{
    /// <inheritdoc />
    public partial class Editnullfieldsmessage : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Message_Files_FileId",
                table: "Message");

            migrationBuilder.AlterColumn<string>(
                name: "FileId",
                table: "Message",
                type: "TEXT",
                nullable: true,
                oldClrType: typeof(string),
                oldType: "TEXT");

            migrationBuilder.AddForeignKey(
                name: "FK_Message_Files_FileId",
                table: "Message",
                column: "FileId",
                principalTable: "Files",
                principalColumn: "Id");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Message_Files_FileId",
                table: "Message");

            migrationBuilder.AlterColumn<string>(
                name: "FileId",
                table: "Message",
                type: "TEXT",
                nullable: false,
                defaultValue: "",
                oldClrType: typeof(string),
                oldType: "TEXT",
                oldNullable: true);

            migrationBuilder.AddForeignKey(
                name: "FK_Message_Files_FileId",
                table: "Message",
                column: "FileId",
                principalTable: "Files",
                principalColumn: "Id",
                onDelete: ReferentialAction.Cascade);
        }
    }
}
